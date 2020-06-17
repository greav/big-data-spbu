package bigdata

import java.io.File

fun main() {
    val bits = listOf(32, 48, 64)
    var result: Long
    var startTime: Long
    var elapsedTime: Long
    val nNumbers = 2000
    val  profilingFile = File("profiling.csv")
    profilingFile.writeText("method,n_numbers,n_bits,result,elapsed_time\n")

    bits.forEach {
        val fileName = "numbers${it}_${nNumbers}.txt"
        generate(fileName, it, nNumbers)

        startTime = System.currentTimeMillis()
        result = sequential(fileName)
        elapsedTime = (System.currentTimeMillis() - startTime)
        profilingFile.appendText("sequential,${nNumbers},${it},${result},${elapsedTime}\n")

        startTime = System.currentTimeMillis()
        result = primitiveFactorization(fileName)
        elapsedTime = (System.currentTimeMillis() - startTime)
        profilingFile.appendText("primitives,${nNumbers},${it},${result},${elapsedTime}\n")

        startTime = System.currentTimeMillis()
        result = rxFactorization(fileName)
        elapsedTime = (System.currentTimeMillis() - startTime)
        profilingFile.appendText("rx,${nNumbers},${it},${result},${elapsedTime}\n")
    }
}