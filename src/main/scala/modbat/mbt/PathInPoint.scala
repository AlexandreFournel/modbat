package modbat.mbt

import modbat.cov.{Trie, TrieNode}
import modbat.dsl.State
import scala.collection.mutable.ListBuffer

case class LabelInfo(label: String,
                     selfTrans: Boolean = false,
                     transQuality: TransitionQuality.Quality =
                       TransitionQuality.OK) // LabelInfo is used for record the label information used for "point" output

/** PathInPoint extends PathVisualizer for showing path coverage in "Point" tree graph.
  *
  * @constructor Create a new pathInPoint with a trie, and shape (Point),
  *
  * @param trie The trie that has path information stored
  * @param shape The shape should be "Point"
  */
class PathInPointGraph(trie: Trie, val shape: String) extends PathVisualizer {
  require(shape == "Point", "the input of path visualizer must be Point")
  override def dotify() {
    out.println("digraph model {")
    out.println("  orientation = landscape;")
    out.println(
      "  graph [ rankdir = \"TB\", ranksep=\"0.3\", nodesep=\"0.2\" ];")
    out.println(
      "  node [ fontname = \"Helvetica\", fontsize=\"6.0\", shape=\"" + shape.toLowerCase +
        "\", margin=\"0.07\"," + " height=\"0.1\" ];")
    out.println(
      "  edge [ fontname = \"Helvetica\", fontsize=\"6.0\"," + " margin=\"0.05\" ];")
    val labelRecorderStack
      : ListBuffer[LabelInfo] = new ListBuffer[LabelInfo] // stack is used for record label information for "point" output
    display(trie.root, 0, labelRecorderStack)
    out.println("}")
  }

  def display(root: TrieNode,
              nodeNumber: Int = 0,
              labelRecorderStack: ListBuffer[LabelInfo] = null)
    : (Int, ListBuffer[LabelInfo]) = {

    var newNodeNumber
      : Int = nodeNumber // newNodeNumber is used to generate the number(ID) of the node for the "point" graph
    var newLabelStack: ListBuffer[LabelInfo] = labelRecorderStack

    if (root.isLeaf) { // print graph when the node in trie is a leaf
      if (newLabelStack != null) {
        // output "point" graph
        var rootPointIsCircle = false // rootPointIsCircle marks if the root point of the current path is a circle or not
        for (i <- newLabelStack.indices) {
          newNodeNumber = newNodeNumber + 1 // update new number for the number point
          if (i == 0) { // starting point
            // check if the root point of the current path is a circle or not
            if (newLabelStack(i).selfTrans || newLabelStack(i).transQuality == TransitionQuality.backtrack) {
              rootPointIsCircle = true // set rootPointIsCircle to true showing the root point is a circle
              newNodeNumber = newNodeNumber - 1 // node number should the same as previous one
              out.println(0 + "->" + 0 + newLabelStack(i).label) // the root point is a circle
            } else {
              out.println(i + "->" + newNodeNumber + newLabelStack(i).label)
            }
          } else if (newLabelStack(i).selfTrans || newLabelStack(i).transQuality == TransitionQuality.backtrack) {
            if (rootPointIsCircle) { // the root point of the current path is a circle
              newNodeNumber = newNodeNumber - 1 // node number should the same as previous one
              out.println(0 + "->" + 0 + newLabelStack(i).label) // same point if self or backtracked transition and
            } else {
              newNodeNumber = newNodeNumber - 1 // node number should the same as previous one
              out.println(newNodeNumber + "->" + newNodeNumber + newLabelStack(
                i).label) // same point if self or backtracked transition
            }
          } else {
            if (rootPointIsCircle) { // the root point of the current path is a circle
              out.println(0 + "->" + newNodeNumber + newLabelStack(i).label)
              rootPointIsCircle = false // next starting point is not the root point again
            } else {
              out.println(
                newNodeNumber - 1 + "->" + newNodeNumber + newLabelStack(i).label)
            }
          }
        }
      }
      if (newLabelStack != null) {
        newLabelStack.trimEnd(1)
      }
      return (newNodeNumber, newLabelStack)
    }

    for (t <- root.children.keySet) {
      val node: TrieNode =
        root.children.getOrElse(t, sys.error(s"unexpected key: $t"))
      val modelName: String = node.modelInfo.modelName
      val modelID = node.modelInfo.modelID.toString
      val transID = node.transitionInfo.transitionID.toString
      val transOriginState: State = node.transitionInfo.transOrigin
      val transDestState: State = node.transitionInfo.transDest
      val transName = transOriginState.toString + " => " + transDestState.toString
      val transQuality: TransitionQuality.Quality =
        node.transitionInfo.transitionQuality
      val transExecutionCounter = node.transitionInfo.transCounter.toString
      // get choices into a string for the output
      /*      val choices: String =
        if (node.transitionInfo.transitionChoices != null) {
          if (node.transitionInfo.transitionChoices.nonEmpty)
            node.transitionInfo.transitionChoices.toList
              .map(_.mkString(", "))
              .mkString("||\\n")
          else "Empty"
        } else "Null"*/

      val selfTransCounter = "(T-Self:" + node.selfTransCounter + ")"
      val edgeStyle: String =
        if (transQuality == TransitionQuality.backtrack)
          "style=dotted, color=red,"
        else ""
      // the newlabel here is used for constructing a label for the output of the "point" graph
      val newLabel = "[" + edgeStyle + "label = \"" + "M:" + modelName + "\\n" +
        "M-ID:" + modelID + "\\n" +
        "T:" + transName + "\\n" +
        "T-ID:" + transID + "\\n" +
        "T-Counter:" + transExecutionCounter + "\\n" +
        // "T-Choices:" + choices + "\\n" +
        selfTransCounter + "\"];"
      // check if the transition has the same original and target states, and if backtracked
      val newlabelInfo =
        if (transOriginState == transDestState && transQuality == TransitionQuality.backtrack)
          LabelInfo(newLabel, true, transQuality)
        else if (transOriginState == transDestState)
          LabelInfo(newLabel, true)
        else if (transQuality == TransitionQuality.backtrack)
          LabelInfo(newLabel, false, transQuality)
        else LabelInfo(newLabel)
      newLabelStack += newlabelInfo // store label information
      val result = display(node, newNodeNumber, newLabelStack)
      newNodeNumber = result._1
      newLabelStack = result._2
    }
    if (newLabelStack != null) {
      newLabelStack.trimEnd(1)
    }
    (newNodeNumber, newLabelStack)
  }

}
