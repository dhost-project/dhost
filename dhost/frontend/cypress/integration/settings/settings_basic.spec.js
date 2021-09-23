describe('My frst tst', function () {
    it('Visit settings', function () {
        cy.visit('http://localhost:3000/ipfs/dhost_v2/settings')
        expect(true).to.equal(true)
        cy.contains('Validate')
        cy.contains('Basic')
    })
})

