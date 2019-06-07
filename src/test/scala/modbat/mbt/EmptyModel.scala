package modbat.mbt

import org.scalatest._

class EmptyModel extends fixture.FlatSpec with fixture.TestDataFixture with Matchers {
  "EmptyModel1" should "fail" in { td =>
    val result = ModbatTestHarness.testMain(Array("-s=1","--no-redirect-out","modbat.test.EmptyModel"), ModbatTestHarness.setTestJar, td)
    result._1 should be(1)
    result._3 shouldBe empty
  }



}
