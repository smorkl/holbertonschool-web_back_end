export default function concatArrays(array1, array2, string) {
  const arrayConca = [...array1, ...array2, ...string];
  return arrayConca
}
