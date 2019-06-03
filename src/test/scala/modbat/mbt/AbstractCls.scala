package modbat.mbt

import org.scalatest._

class AbstractCls extends FlatSpec with Matchers {
  "AbstractCls1" should "pass" in {
    val result = ModbatTestHarness.testMain(Array("-s=1","--no-redirect-out","modbat.test.AbstractCls"), ModbatTestHarness.setTestJar)
    result._1 should be(0)
    result._3 shouldBe empty
  }



}