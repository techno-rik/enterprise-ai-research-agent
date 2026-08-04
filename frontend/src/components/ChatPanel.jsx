import { useState } from "react";
import { MessageSquare } from "lucide-react";

import { askQuestion } from "../services/api";
import AnswerCard from "./AnswerCard";


export default function ChatPanel() {

    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [loading, setLoading] = useState(false);


    const handleAsk = async () => {

        if (!question.trim()) return;

        setLoading(true);
        setAnswer("");

        try {

            const result = await askQuestion(question);

            setAnswer(result.answer);

            setQuestion("");

        } catch (error) {

            console.error("Chat Error:", error);

            setAnswer(
                "Sorry, I couldn't generate an answer. Please try again."
            );

        } finally {

            setLoading(false);

        }

    };


    const handleKeyDown = (event) => {

        if (event.key === "Enter" && !loading) {
            handleAsk();
        }

    };


    return (

        <div className="research-card">

            <h2 className="section-heading">

                <MessageSquare size={22} />

                Ask Questions About This Research

            </h2>


            <p className="chat-description">
                Ask follow-up questions using the generated research
                and knowledge base.
            </p>


            <div className="research-form">

                <input
                    type="text"
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    onKeyDown={handleKeyDown}
                    placeholder="Ask a follow-up question..."
                    disabled={loading}
                />

                <button
                    onClick={handleAsk}
                    disabled={loading || !question.trim()}
                >

                    {loading ? "Thinking..." : "Ask"}

                </button>

            </div>


            {loading && (

                <div className="thinking-indicator">

                    <span></span>
                    <span></span>
                    <span></span>

                    <p>InsightForge AI is thinking</p>

                </div>

            )}


            <AnswerCard answer={answer} />

        </div>

    );

}