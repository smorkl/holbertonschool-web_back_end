const weakMap = new WeakMap();

export default function queryAPI(endpoint) {
  const count = weakMap.get(endpoint) || 0;

  if (count >= 5) {
    throw new Error('Endpoint load is high');
  }

  weakMap.set(endpoint, count + 1);

  // Simulate API call (replace with actual API call)
  console.log(`Querying ${endpoint.name}...`);
  return Promise.resolve('Data fetched');
}