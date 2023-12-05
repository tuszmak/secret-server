import Link from "next/link";
import React, { useEffect, useState } from "react";

export default function getSecret() {
  const [hash, setHash] = useState<string>("");
  const [secretString, setSecretString] = useState<string>("");
  const getSecret = async () => {
    const request: SecretFetchRequest = {
      hash: hash,
    };
    const response = await fetch("/api/v1/getSecret", {
      body: JSON.stringify(request),
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const secret: Secret = await response.json();
    setSecretString(secret.secret);
  };
  return secretString ? (
    <div>
      <button>
        <Link href="/">Back</Link>
      </button>
      <div>
        Your secret is: {secretString}
      </div>
    </div>
  ) : (
    <div>
      <button>
        <Link href="/">Back</Link>
      </button>
      <label htmlFor="hash">Input hash</label>
      <input
        type="text"
        name="hash"
        id="hash"
        onChange={(e: React.FormEvent<HTMLInputElement>) =>
          setHash(e.currentTarget.value)
        }
        value={hash}
      />
      <button onClick={() => getSecret()}>Submit</button>
    </div>
  );
}
