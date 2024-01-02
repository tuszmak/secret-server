import BackButton from "@/components/BackButton"
import {render, screen} from "@testing-library/react"
import '@testing-library/jest-dom'


it('should have "Back" text', ()=>{
    render(<BackButton />)
    const button = screen.getByText("Back")
    expect(button).toBeInTheDocument()
})

it("Should have a button", ()=>{
    render(<BackButton />)
    const button = screen.getByRole("button")
    expect(button).toBeInTheDocument()


})