package bigdata
import java.io.File
import java.math.BigInteger


fun generate(file_name: String, numBits: Int, nNumbers: Int){
    val file = File(file_name)
    for (i in 1..nNumbers) {
        val number = BigInteger(numBits, java.util.Random())
        file.appendText("$number\n")
    }

}