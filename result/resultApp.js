const express = require("express");
const { Client } = require("pg");

const app = express();
const client = new Client({
  user: "postgres",
  host: "db",
  database: "postgres",
  password: "postgres",
  port: 5432,
});

client.connect();

app.get("/", async (req, res) => {
  const result = await client.query("SELECT vote, COUNT(*) AS count FROM votes GROUP BY vote");
  res.json(result.rows);
});

app.listen(80, () => {
  console.log("Result app running on port 80");
});