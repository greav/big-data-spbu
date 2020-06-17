package bigdata

import java.io.File
import java.math.BigInteger
import java.util.concurrent.atomic.AtomicLong
import java.util.concurrent.locks.ReentrantLock


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
