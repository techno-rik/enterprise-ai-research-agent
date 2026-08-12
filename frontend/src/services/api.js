const API_BASE = "https://enterprise-ai-research-agent.onrender.com";

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
        `${API_BASE}/chat`,
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