import React from "react";

function LogsTable({ logs }) {
	return (
		<table>
			<thead>
				<tr>
					<th>Job ID</th>
					<th>Run Length (s)</th>
					<th>Executor Count</th>
					<th>Operators</th>
					<th>Errors</th>
				</tr>
			</thead>
			<tbody>
				{logs.map((log) => (
					<tr key={log.job_id}>
						<td>{log.job_id}</td>
						<td>{log.run_length}</td>
						<td>{log.executor_count}</td>
						<td>{log.operators.join(", ")}</td>
						<td>{log.errors.length > 0 ? log.errors.join(", ") : "No errors"}</td>
					</tr>
				))}
			</tbody>
		</table>
	);
}

export default LogsTable;
