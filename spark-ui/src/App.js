import React, { useState, useEffect } from "react";
import axios from "axios";
import LogsTable from "./LogsTable";
import Loading from "./Loading";
import "./App.css";

function App() {
	const [logs, setLogs] = useState([]);
	const [loading, setLoading] = useState(true);

	useEffect(() => {
		axios.get("http://localhost:8000/logs/")
			.then(response => {
				setLogs(response.data);
				setLoading(false);
			})
			.catch(error => {
				console.error("Error fetching logs:", error);
				setLoading(false);
			});
	}, []);

	return (
		<div>
			<h1>Spark Job Logs</h1>
			{loading ? <Loading /> : <LogsTable logs={logs} />}
		</div>
	);
}

export default App;