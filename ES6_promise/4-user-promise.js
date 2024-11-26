function signUpUser(firstName, lastName) {
  return Promise
    .then((userResult) => {
      const [{ body }, { firstName, lastName }] = userResult;

      console.log(`${body} ${firstName} ${lastName}`);
    })
}