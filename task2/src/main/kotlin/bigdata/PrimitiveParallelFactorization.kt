package bigdata

import java.io.File
import java.math.BigInteger
import java.util.concurrent.CompletableFuture
import java.util.concurrent.Executors
import java.util.concurrent.atomic.AtomicLong
import java.util.concurrent.locks.ReentrantLock
import java.util.function.Supplier
import java.util.stream.Collectors.toList


fun primitiveFactorization(fileName: String,
                           numThreads: Int = Runtime.getRuntime().availableProcessors()): Long {
    val numbers = File(fileName).readLines().map { it.toBigInteger() }
    val result = AtomicLong(0)
    val lock = ReentrantLock()
    var curIndex = 0
    var number: BigInteger

    val threads = List(numThreads) {
        Thread(Runnable {
            var threadResult: Long = 0
            while (curIndex < numbers.size) {
                try {
                    lock.lock()
                    number = numbers[curIndex]
                    curIndex++
                } finally {
                    lock.unlock()
                }
                threadResult += factorize(number)
            }
            result.addAndGet(threadResult)
        })
    }

    for (thread in threads)
        thread.start()

    for (thread in threads)
        thread.join()
    return result.toLong()
}


fun futureFactorization(fileName: String,
                                   numThreads: Int = Runtime.getRuntime().availableProcessors()): Long {
    val numbers = File(fileName).readLines().map { it.toBigInteger() }
    val executor = Executors.newFixedThreadPool(numThreads)
    var result: Long = 0

    val futures = numbers.parallelStream()
            .map { i: BigInteger -> CompletableFuture.supplyAsync(Supplier { factorize(i) }, executor) }.collect(toList())

    futures.forEach{
        result += it.get()
    }
    executor.shutdown()

    return result
}