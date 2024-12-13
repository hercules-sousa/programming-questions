val table = arrayOf(4.0, 4.5, 5.0, 2.0, 1.5)

val line = readLine()
val values = line?.split(" ")
val code = values?.get(0)?.toIntOrNull() ?: 0
val qtd = values?.get(1)?.toDoubleOrNull() ?: 0.0
val pos = code - 1
val result = table.get(pos) * qtd
val formatted = String.format("%.2f", result).replace(",", ".")

println("Total: R$ $formatted")