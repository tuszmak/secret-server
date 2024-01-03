import { getByRole, render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import { userEvent } from "@testing-library/user-event";
import Home from "@/pages";
import { describe } from "node:test";

describe("Render", ()=>{
    it("Should have a heading", ()=>{
        render(<Home />)
        const title = screen.getByRole("heading")
        expect(title).toBeInTheDocument()
    })
    it("Should have a heading with 'Hello there in it'", ()=>{
        render(<Home />)
        const title = screen.getByText("Hello there")
        expect(title).toBeInTheDocument()
    })
    //This test is temporary, as is the sample text.
    it("Should have a paragraph with sample text in it", ()=>{
        render(<Home />)
        const paragraph = screen.getByText(/Provident/i)
        expect(paragraph).toBeInTheDocument()
    })
    it("Should have a button, with create secret text", ()=>{
        render(<Home />)
        const createButton = screen.getByText("Create secret")
        expect(createButton).toBeInTheDocument()
    })
    it('Should have a button, with "view secret" text', ()=>{
        render(<Home />)
        const viewButton = screen.getByText("View secret")
        expect(viewButton).toBeInTheDocument()
    })
})
describe("Behavior", ()=>{
    
})