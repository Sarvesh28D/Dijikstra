function findShortestPath() {
    const graphInput = document.getElementById('graphInput').value;
    const startNode = document.getElementById('startNode').value;
    const resultDiv = document.getElementById('result');

    resultDiv.textContent = 'Calculating... ⏳';  // Show loading message

    try {
        const graph = JSON.parse(graphInput);

        fetch('http://127.0.0.1:5000/dijkstra', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ graph, start: startNode }),
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.textContent = '⚠️ Failed to fetch result. Please try again.';
        });

    } catch (error) {
        resultDiv.textContent = '⚠️ Invalid JSON input!';
    }
}
