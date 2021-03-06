package modbat.test

import modbat.dsl._

class GenLabel3 extends Model {
  var n = 0

  @States(Array("init")) def inc() { n = n + 1 }

  @States(Array("init")) def dec() { n = n - 1; assert (n > 0) }

  "init" -> "init" := skip
}
