import BackButton from "@/components/BackButton";
import ExpiryDateInput from "@/components/ExpiryDateInput";
import NumberInput from "@/components/NumberInput";
import TextInput from "@/components/TextInput";
import Link from "next/link";
import React, { useState } from "react";

type SecretCreationData = {
  secret: string;
  numberOfVisits: number;
  expiryDate: string;
};
function save() {
  const [secret, setSecret] = useState<string>("");
  const [numberOfVisits, setNumberOfVisits] = useState<number>(0);
  const [expiryDate, setExpiryDate] = useState<string>("");
  const [link, setLink] = useState<string>("");
  const handleSubmit = async () => {
    const data: SecretCreationData = {
      secret,
      numberOfVisits,
      expiryDate,
    };
    const response = await fetch("/api/v1/secret", {
      method: "POST",
      body: JSON.stringify(data),
    });
    if (response.ok) {
      console.log("yay!");
      const responseLink = await response.text();
      setLink(responseLink);
    }
  };

  return link ? (
    <div>
      <div><BackButton></BackButton></div>
      Your secret link is: {link}. Keep it a secret!</div>
  ) : (
    <div>
      <div><BackButton></BackButton></div>
      <div className="flex flex-col items-center gap-3">
      <TextInput handleChange={(e: string) => setSecret(e)} />
      <NumberInput handleChange={(e: number) => setNumberOfVisits(e)} />
      <ExpiryDateInput handleChange={(e: string) => setExpiryDate(e)} />
      <button className="btn btn-primary mt-8" onClick={handleSubmit}>
        Submit
      </button>
    </div>
    </div>
  );
}

export default save;
