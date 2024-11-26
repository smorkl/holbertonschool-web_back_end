import { uploadPhoto, createUser } from "./utils";

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((userResult) => {
      const [{ body}, {firstName, lastName}] = userResult;

      console.log(`${body} ${firstName} ${lastName}`);
    })
    .catch((error) => {
      console.log("Signup system offline");
    });
}
