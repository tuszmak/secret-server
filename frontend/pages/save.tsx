import ExpiryDateInput from "@/components/ExpiryDateInput";
import NumberInput from "@/components/NumberInput";
import TextInput from "@/components/TextInput";
import React, { useState } from "react";

type SecretCreationData = {
    secret: string,
    numberOfVisits : number,
    expiryDate : string
}
function save() {
  const [secret, setSecret] = useState<string>("");
  const [numberOfVisits, setNumberOfVisits] = useState<number>(0);
  const [expiryDate, setExpiryDate] = useState<string>("");
  const handleSubmit = async()=>{
    const data : SecretCreationData = {
        secret, numberOfVisits, expiryDate
    } 
    const response = await fetch("/api/createSecret",{
      method: "POST",
      body: JSON.stringify(data)
    })
    if(response.ok) console.log("yay!");
    
  }
  
  return (
    <div className="flex flex-col items-center gap-3">
      <TextInput handleChange={(e:string)=>setSecret(e)} />
      <NumberInput handleChange={(e: number) => setNumberOfVisits(e)} />
      <ExpiryDateInput handleChange={(e: string)=> setExpiryDate(e)} />
      <button className="btn btn-primary mt-8" onClick={handleSubmit}>Submit</button>
    </div>
  );
}

export default save;
