const apiUrl =
  "https://4osypyoex4.execute-api.us-east-1.amazonaws.com/prod/myVisitorCounter";

fetch(apiUrl)
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network Error");
    }
    return response.json();
  })
  .then((data) => {
    console.log(data);
    document.querySelector(
      "p#viewscounter"
    ).innerHTML = `There are ${data["views"]} views`;
  })
  .catch((error) => {
    console.error("Error:", error);
  });
