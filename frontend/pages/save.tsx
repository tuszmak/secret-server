import ExpiryDateInput from '@/components/ExpiryDateInput';
import NumberInput from '@/components/NumberInput'
import TextInput from '@/components/TextInput'
import React, {useState} from 'react'

function save() {
    const [secret, setSecret] = useState<string>("");
  return (
    <div className='flex flex-col items-center gap-3'>
        <TextInput />
        <NumberInput />
        <ExpiryDateInput />
        <button className='btn btn-primary mt-8'>Submit</button>
    </div>
  )
}

export default save