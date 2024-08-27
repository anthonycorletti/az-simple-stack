import { expect, test } from 'vitest'
import { render, screen } from "@testing-library/react"
import Page from "../app/page"

test("Page", () => {
  render(<Page />)
  const linkElement = screen.getByText(/Docs/)
  expect(linkElement).toBeDefined()
})
