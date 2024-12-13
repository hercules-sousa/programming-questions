val input1 = readLine()?.toDoubleOrNull() ?: 0.0
val input2 = readLine()?.toDoubleOrNull() ?: 0.0

val result = (input1 * 3.5 + input2 * 7.5) / 11
val formatted = String.format("%.5f", result).replace(",", ".")

println("MEDIA = $formatted")