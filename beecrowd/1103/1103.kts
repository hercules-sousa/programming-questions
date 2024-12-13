val MINUTES_IN_A_DAY = 1440

var input = readLine()
    
    while(input != "0 0 0 0") {
        val splitted = input?.split(" ")
        val h1 = splitted?.get(0)?.toIntOrNull() ?: 0
        val m1 = splitted?.get(1)?.toIntOrNull() ?: 0
        val h2 = splitted?.get(2)?.toIntOrNull() ?: 0
        val m2 = splitted?.get(3)?.toIntOrNull() ?: 0
    
        val minutes1 = h1 * 60 + m1
        var minutes2 = h2 * 60 + m2
    
        if (minutes2 < minutes1) {
            minutes2 += MINUTES_IN_A_DAY
        }
    
        println(minutes2 - minutes1)
    
        input = readLine()
    }