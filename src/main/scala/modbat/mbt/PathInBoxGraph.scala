package modbat.mbt

import modbat.cov.{Trie, TrieNode}

import scala.collection.mutable.ListBuffer

case class NodeInfo(node: TrieNode, var transCounter: String) // NodeInfo is used for record  the node information used for "box" output

/** PathInBox extends PathVisualizer for showing path coverage in "Box" tree graph.
  *
  * @constructor Create a new pathInBox with a trie, and shape (Box),
  *
  * @param trie The trie that has path information stored
  * @param shape The shape should be "Box"
  */
class PathInBoxGraph(trie: Trie, val shape: String) extends PathVisualizer {
  require(shape == "Box", "the input of path visualizer must be Box")

  override def dotify() {
    out.println("digraph model {")
    out.println("  orientation = landscape;")
    out.println("  graph [ rankdir = \"TB\", ranksep=\"2\", nodesep=\"0.2\" ];")
    out.println(
      "  node [ fontname = \"Helvetica\", fontsize=\"6.0\", style=rounded, shape=\"" + shape.toLowerCase +
        "\", margin=\"0.07\"," + " height=\"0.1\" ];")
    out.println(
      "  edge [ fontname = \"Helvetica\", arrowsize=\".3\", arrowhead=\"vee\", fontsize=\"6.0\"," + " margin=\"0.05\" ];")

    val nodeRecorder
      : ListBuffer[NodeInfo] = new ListBuffer[NodeInfo] // nodeRecorder is used for record node information for "box" output
    display(trie.root, 0, nodeRecorder)
    out.println("}")
  }

  private def display(root: TrieNode,
                      level: Int = 0,
                      nodeRecorder: ListBuffer[NodeInfo] = null): Unit = {

    if (root.isLeaf) return

    for (t <- root.children.keySet) {
      val node: TrieNode =
        root.children.getOrElse(t, sys.error(s"unexpected key: $t"))

      var sameTransition = false
      if (nodeRecorder != null) {
        for (n <- nodeRecorder) {
          // the transition already in the nodeRecorder, and the transition quality is also the same
          if (n.node.transitionInfo.transitionID == node.transitionInfo.transitionID &&
              n.node.transitionInfo.transitionQuality == node.transitionInfo.transitionQuality) {
            sameTransition = true
            // merge the value of the transition counter
            n.transCounter = n.transCounter.concat(
              ";" + node.transitionInfo.transCounter.toString)

            // merge the counter in map of choices
            for (key <- node.transitionInfo.transitionChoicesMap.keySet) {
              if (n.node.transitionInfo.transitionChoicesMap.contains(key)) {
                val mergedChoiceCoutner = n.node.transitionInfo
                  .transitionChoicesMap(key) +
                  node.transitionInfo.transitionChoicesMap(key)
                n.node.transitionInfo.transitionChoicesMap(key) =
                  mergedChoiceCoutner
              }
            }
          }
        }
      }

      if (!sameTransition) {
        val newNodeInfo =
          NodeInfo(node, node.transitionInfo.transCounter.toString)
        nodeRecorder += newNodeInfo
      }

      display(node, level + 1, nodeRecorder)
      // TODO: I think there's no need to repeat the same father node in the graph - Rui
    }

    // output "box" graph
    if (level == 0 && nodeRecorder != null && nodeRecorder.nonEmpty) {
      drawBoxGraph(nodeRecorder)
    }
  }

  private def drawBoxGraph(nodeRecorder: ListBuffer[NodeInfo]): Unit = {

    for (n <- nodeRecorder) {
      val transOrigin: String = n.node.transitionInfo.transOrigin.toString
      val transDest: String = n.node.transitionInfo.transDest.toString
      val transName: String = transOrigin + " => " + transDest
      val transitionID: String = n.node.transitionInfo.transitionID.toString
      val modelName: String = n.node.modelInfo.modelName
      val modelID: String = n.node.modelInfo.modelID.toString
      val edgeStyle: String =
        if (n.node.transitionInfo.transitionQuality == TransitionQuality.backtrack)
          "style=dotted, color=red,"
        else ""
      if (n.node.transitionInfo.transitionQuality == TransitionQuality.backtrack)
        out.println(" " + transDest + " [color=red];")

      // choiceTree can record choices
      val choiceTree: ChoiceTree = new ChoiceTree()

      if (n.node.transitionInfo.transitionChoicesMap != null && n.node.transitionInfo.transitionChoicesMap.nonEmpty) {
        // transition with choices
        for ((choiceList, counter) <- n.node.transitionInfo.transitionChoicesMap) {
          // insert choices and choice counter into choiceTree
          choiceTree.insert(choiceList, counter)
        }
        // draw Choices with transitions
        drawTransWithChoices(n, choiceTree.root, 0, "")
        //choiceTree.display(choiceTree.root, 0)
      } else {
        // transitions without choices
        out.println(
          transOrigin + "->" + transDest +
            "[" + edgeStyle + "label = \"" + "M:" + modelName + "\\n" +
            "M-ID:" + modelID + "\\n" +
            "T:" + transName + "\\n" +
            "T-ID:" + transitionID + "\\n" +
            "T-Counter:" + n.transCounter + "\\n" +
            "(T-Self:" + n.node.selfTransCounter + ")" + "\"];")
      }
    }
  }

  private def drawTransWithChoices(
      nodeInfo: NodeInfo,
      root: ChoiceTree#ChoiceNode /*this.ChoiceTree#ChoiceNode*/,
      level: Int = 0,
      currentNodeID: String): Unit = {

    val transOrigin: String = nodeInfo.node.transitionInfo.transOrigin.toString
    val transDest: String = nodeInfo.node.transitionInfo.transDest.toString
    val transName: String = transOrigin + " => " + transDest
    val edgeStyle: String =
      if (nodeInfo.node.transitionInfo.transitionQuality == TransitionQuality.backtrack)
        "style=dotted, color=red,"
      else ""
    val modelName: String = nodeInfo.node.modelInfo.modelName
    val modelID: String = nodeInfo.node.modelInfo.modelID.toString
    val transitionID: String =
      nodeInfo.node.transitionInfo.transitionID.toString
    val label: String = "[" + edgeStyle + "label = \"" +
      "M:" + modelName + "\\n" +
      "M-ID:" + modelID + "\\n" +
      "T:" + transName + "\\n" +
      "T-ID:" + transitionID + "\\n" +
      "T-Counter:" + nodeInfo.transCounter + "\\n" +
      "(T-Self:" + nodeInfo.node.selfTransCounter + ")" + "\"];"

    if (root.isLeaf) out.println(currentNodeID + "->" + transDest + label)

    for (choiceKey <- root.children.keySet) {
      val choiceNode = root.children(choiceKey)

      val choiceNodeStyle: String =
        " , shape=diamond, width=0.1, height=0.1, xlabel=\"Choice-Counter:" + choiceNode.choiceCounter + "\"];"
      val destNodeValue = choiceNode.recordedChoice.toString
      val destNodeID = "\"" + transitionID + "-" + level.toString + "-" + destNodeValue + "\""
      out.println(
        destNodeID + " [label=\"" + destNodeValue + "\"" + choiceNodeStyle)

      if (level == 0) {
        out.println(transOrigin + "->" + destNodeID + label)
      } else {
        out.println(currentNodeID + "->" + destNodeID + label)
      }

      drawTransWithChoices(nodeInfo, choiceNode, level + 1, destNodeID)
    }
  }
}
