import React, { Component } from 'react';

class Purchase extends Component {

// Everything needs to be inside the "App" div
  render() {
    return (
        <a href="#" className="list-group-item">{this.props.purchase.date} - <strong>{this.props.purchase.vendor}</strong> - {this.props.purchase.price}</a>

    );
  }
}

export default Purchase;
