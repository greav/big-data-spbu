package bigdata
import java.math.BigInteger


fun factorize(number: BigInteger): Long {
    var number = number
    var count: Long = 0
    var factor = BigInteger.TWO
    while (number.remainder(factor) == BigInteger.ZERO) {
        count++
        number = number.divide(factor)
    }
    factor++

    while (factor * factor <= number) {

        if (number.remainder(factor) == BigInteger.ZERO) {
            count++
            number = number.divide(factor)
        } else {
            factor += BigInteger.TWO
        }
    }
    count++

    return count
}
