package bigdata

import java.io.File
import java.math.BigInteger

fun sequential(fileName: String) : Long {
    val file = File(fileName)
    var count: Long = 0
    file.forEachLine {
        count += factorize(BigInteger(it))
    }
    return count
}