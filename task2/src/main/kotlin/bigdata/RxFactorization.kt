package bigdata

import io.reactivex.Flowable
import io.reactivex.schedulers.Schedulers
import java.io.File


fun rxFactorization(fileName: String): Long {
    val numbers = File(fileName).readLines().map { it.toBigInteger() }
    return Flowable.fromIterable(numbers)
            .onBackpressureBuffer()
            .parallel()
            .runOn(Schedulers.computation())
            .map { number -> factorize(number) }
            .sequential()
            .reduceWith({ 0 }, { acc: Long, item: Long -> acc + item })
            .blockingGet()
}
