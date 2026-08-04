const API_BASE = "http://127.0.0.1:8000";

export async function createResearch(topic) {

    const response = await fetch(
        `${API_BASE}/research`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify({
                topic,
            }),
        }
    );

    return await response.json();
}

export async function askQuestion(question) {

    const response = await fetch(
        "http://127.0.0.1:8000/chat",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify({
                question,
            }),
        }
    );

    return await response.json();
}