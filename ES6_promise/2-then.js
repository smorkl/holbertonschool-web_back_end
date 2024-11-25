export default function handleResponseFromAPI(promise) {
  return new Promise((res, reject) => {
    if (promise) {
      res({
        status: 200,
        body: 'Success',
      });
    } else {
      reject(Error('Got a response from the API'));
    }
  });
}
