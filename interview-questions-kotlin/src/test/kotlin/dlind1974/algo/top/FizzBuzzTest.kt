package dlind1974.algo.top

import kotlin.test.Test
import kotlin.test.assertEquals

private fun fizzBuzz(n: Int): List<String> {
    var result = mutableListOf<String>()

    for (i in 1..n) {
        if (i % 15 == 0) result.add("FizzBuzz")
        else if (i % 3 == 0) result.add("Fizz")
        else if (i % 5 == 0) result.add("Buzz")
        else result.add(i.toString())
    }

    return result
}

private fun fizzBuzzIdiomatic(n: Int): List<String> = List<String>(n) { i ->
    val index = i + 1
    when {
        index % 15 == 0 -> "FizzBuzz"
        index % 3 == 0 -> "Fizz"
        index % 5 == 0 -> "Buzz"
        else -> index.toString()
    }
}

class FizzBuzzTest {

    @Test
    fun testN3() {
        val actual = fizzBuzzIdiomatic(3)
        val expected = listOf("1","2","Fizz")
        assertEquals(expected, actual)
    }

    @Test
    fun testN5() {
        val actual = fizzBuzzIdiomatic(5)
        val expected = listOf("1","2","Fizz","4","Buzz")
        assertEquals(expected, actual)
    }

    @Test
    fun testN15() {
        val actual = fizzBuzzIdiomatic(15)
        val expected = listOf("1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz")
        assertEquals(expected, actual)
    }
}