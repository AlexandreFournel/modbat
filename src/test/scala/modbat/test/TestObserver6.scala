package modbat.test

import modbat.dsl._

class TestObserver6(val target: CounterModel) extends Observer {
  def this() = this(null)

  // transitions
  "zero" -> "one" := {
    require(target.i > 0)
    assert(MockEnv.nonDetCall)
    Console.out.println("one")
  }
  "one" -> "many" := {
    require(target.i > 1)
    Console.out.println("many")
  }
  "many" -> "many" := {
    assert(target.i < 4)
  }
}
