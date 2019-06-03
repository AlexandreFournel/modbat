package modbat.mbt

import org.scalatest._

class CrashSoon extends FlatSpec with Matchers {
  "CrashSoon1" should "pass" in {
    val result = ModbatTestHarness.testMain(Array("-s=1","-n=200","--no-redirect-out","--stop-on-failure","modbat.test.CrashSoon"), ModbatTestHarness.setTestJar)
    result._1 should be(0)
    result._3 shouldBe empty
  }



}