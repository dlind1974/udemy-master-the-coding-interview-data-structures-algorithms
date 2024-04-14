package dlind1974.algo.top

import kotlin.test.Test
import kotlin.test.assertEquals

private fun singleNumber(nums: IntArray): Int {
    return nums.reduce { acc, num -> acc xor num }
}

class SingleNumberTest {

    @Test
    fun testSingleNumberTc1() {
        val nums = intArrayOf(2,2,1)
        val actual = singleNumber(nums)
        assertEquals(1, actual)
    }

    @Test
    fun testSingleNumberTc2() {
        val nums = intArrayOf(4, 1, 2, 1, 2)
        val actual = singleNumber(nums)
        assertEquals(4, actual)
    }
}