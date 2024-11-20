export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw Error('Cannot process');
  const copy = new Map(map); // Create a copy of the original Map
  for (const [k, v] of copy.entries()) {
    if (v === 1) {
    copy.set(k, 100);
    }
  }
  return copy;
}
