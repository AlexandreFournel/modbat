package modbat.mbt

import org.scalatest._

class CounterPosNeg extends fixture.FlatSpec with fixture.TestDataFixture with Matchers {
  "CounterPosNeg1" should "pass" in { td =>
    val result = ModbatTestHarness.testMain(Array("--mode=dot","--auto-labels","modbat.examples.CounterPosNeg"), ModbatTestHarness.setExamplesJar, td, Some("modbat.examples.CounterPosNeg.dot","counterpn.dot"))
    result._2 shouldBe empty
  }
}
