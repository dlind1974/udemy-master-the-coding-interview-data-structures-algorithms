package dlind1974.algo.top

import kotlin.math.max
import kotlin.test.Test
import kotlin.test.assertEquals

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

private fun maxDepth(root: TreeNode?): Int {
    if (root == null) return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
}

private fun maxDepthIdiomatic(root: TreeNode?): Int =
    root?.let { 1 + max(maxDepthIdiomatic(it.left), maxDepthIdiomatic(it.right)) } ?: 0


private fun createTreeTc1(): TreeNode {
    val root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right!!.left = TreeNode(25)
    root.right!!.right = TreeNode(7)
    return root
}

class MaxDepthBinaryTreeTest {

    @Test
    fun testTc1() {
        val tree = createTreeTc1()
        val actualDepth = maxDepth(tree)
        assertEquals(3, actualDepth)

        val actualDepth2 = maxDepthIdiomatic(tree)
        assertEquals(3, actualDepth2)

    }
}