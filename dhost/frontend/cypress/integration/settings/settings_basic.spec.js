describe('My frst tst', function () {
    it('Visit settings', function () {
        cy.visit('http://localhost:3000/ipfs/dhost_v2')
        cy.contains('Settings').click()
        cy.url().should('include', '/settings')
        expect(true).to.equal(true)
        cy.contains('Validate')
        cy.contains('Basic')
        cy.contains('Build')
        cy.contains('Github')
        cy.contains('Environment variables')
        cy.get('#basic').click()
        cy.contains("Change done.")
        cy.wait(1000)
        cy.get('#build').click()
        cy.contains("Change done.")
        cy.wait(1000)
        cy.get('#github').click()
        cy.contains("Change done.")
        cy.wait(1000)
        cy.get('#var').click()
        cy.contains("Change done.")

    })
})

