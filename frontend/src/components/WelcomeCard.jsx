import {
    Search,
    Bot,
    Database,
    Globe
} from "lucide-react";

export default function WelcomeCard() {

    const examples = [
        "Artificial Intelligence in Banking",
        "AI Infrastructure Cost",
        "Cloud Security Best Practices",
        "Zero Trust Architecture",
        "Kubernetes Security",
        "Generative AI in Healthcare"
    ];

    return (

        <div className="research-card welcome-card">

            <h2>Welcome to InsightForge AI</h2>

            <p className="welcome-text">
                Generate enterprise-grade research reports powered by
                web search, Large Language Models, and vector search.
            </p>

            <div className="welcome-features">

                <div className="feature-item">
                    <Search size={20} />
                    <span>Real-time Web Research</span>
                </div>

                <div className="feature-item">
                    <Bot size={20} />
                    <span>AI Executive Summaries</span>
                </div>

                <div className="feature-item">
                    <Database size={20} />
                    <span>Vector Knowledge Base</span>
                </div>

                <div className="feature-item">
                    <Globe size={20} />
                    <span>Source-backed Answers</span>
                </div>

            </div>

            <h3 style={{ marginTop: "30px" }}>
                Try one of these topics
            </h3>

            <div className="example-grid">

                {examples.map((example, index) => (

                    <div
                        key={index}
                        className="example-chip"
                    >
                        {example}
                    </div>

                ))}

            </div>

        </div>

    );

}