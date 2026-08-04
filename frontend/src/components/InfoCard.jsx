import { CheckCircle } from "lucide-react";

export default function InfoCard({ title, items }) {

    return (

        <div className="research-card">

            <h2
                style={{
                    display:"flex",
                    alignItems:"center",
                    gap:"10px"
                }}
            >

                <CheckCircle size={20}/>

                {title}

            </h2>

            <ul className="info-list">

                {

                    items.map((item,index)=>(

                        <li key={index}>
                            {item}
                        </li>

                    ))

                }

            </ul>

        </div>

    );

}