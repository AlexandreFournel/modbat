package modbat.mbt

import org.scalatest._

class MaybeTest extends FlatSpec with Matchers {
  "MaybeTest1" should "pass" in {
    val result = ModbatTestHarness.testMain(Array("-s=1","-n=1","modbat.test.MaybeTest","--maybe-probability=0.0","--no-redirect-out"), ModbatTestHarness.setTestJar)
    result._1 should be(0)
    result._3 shouldBe empty
  }



  "MaybeTest2" should "pass" in {
    val result = ModbatTestHarness.testMain(Array("-s=1","-n=1","modbat.test.MaybeTest","--maybe-probability=1.0","--no-redirect-out"), ModbatTestHarness.setTestJar)
    result._1 should be(0)
    result._3 shouldBe empty
  }



  "MaybeTest3" should "pass" in {
    val result = ModbatTestHarness.testMain(Array("-s=1","-n=100","modbat.test.MaybeTest","--maybe-probability=0.01","--no-redirect-out"), ModbatTestHarness.setTestJar)
    result._1 should be(0)
    result._3 shouldBe empty
  }



}