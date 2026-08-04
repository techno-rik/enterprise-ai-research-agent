import { Bot } from "lucide-react";

export default function AnswerCard({ answer }) {

    if (!answer) return null;

    return (

        <div className="answer-card">

            <div className="answer-header">

                <Bot size={20} />

                <h3>InsightForge AI</h3>

            </div>

            <div className="answer-content">

                <p>{answer}</p>

            </div>

        </div>

    );

}