import "./Payment.css"

export function Payment() {
  return (
    <div className="payment mt-3">
      <div className="col-75">
        <div className="container">
          <form>
            <div className="row">
              <div className="col-50">
                <h1 className="text-2xl mb-4">Billing Address</h1>
                <label>
                  <i className="fa fa-user"></i> Full Name
                </label>
                <input
                  type="text"
                  id="fname"
                  name="firstname"
                  placeholder="John M. Doe"
                />
                <label>
                  <i className="fa fa-envelope"></i> Email
                </label>
                <input
                  type="text"
                  id="email"
                  name="email"
                  placeholder="john@example.com"
                />
                <label>
                  <i className="fa fa-address-card-o"></i> Address
                </label>
                <input
                  type="text"
                  id="adr"
                  name="address"
                  placeholder="542 W. 15th Street"
                />
                <label>
                  <i className="fa fa-institution"></i> City
                </label>
                <input
                  type="text"
                  id="city"
                  name="city"
                  placeholder="New York"
                />

                <div className="row">
                  <div className="col-50">
                    <label>State</label>
                    <input
                      type="text"
                      id="state"
                      name="state"
                      placeholder="NY"
                    />
                  </div>
                  <div className="col-50">
                    <label>Zip</label>
                    <input
                      type="text"
                      id="zip"
                      name="zip"
                      placeholder="10001"
                    />
                  </div>
                </div>
              </div>

              <div className="col-50">
                <h1 className="text-2xl mb-4">Payment</h1>
                <label>Name on Card</label>
                <input
                  type="text"
                  id="cname"
                  name="cardname"
                  placeholder="John More Doe"
                />
                <label>Credit card number</label>
                <input
                  type="text"
                  id="ccnum"
                  name="cardnumber"
                  placeholder="1111-2222-3333-4444"
                />
                <label>Exp Month</label>
                <input
                  type="text"
                  id="expmonth"
                  name="expmonth"
                  placeholder="September"
                />
                <div className="row">
                  <div className="col-50">
                    <label>Exp Year</label>
                    <input
                      type="text"
                      id="expyear"
                      name="expyear"
                      placeholder="2018"
                    />
                  </div>
                  <div className="col-50">
                    <label>CVV</label>
                    <input type="text" id="cvv" name="cvv" placeholder="352" />
                  </div>
                </div>
              </div>
            </div>
            <input type="submit" value="Continue to checkout" className="btn" />
          </form>
        </div>
      </div>
    </div>
  )
}
