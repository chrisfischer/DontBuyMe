import React from 'react'
import { Bar } from 'react-chartjs-2'

class Graph extends React.Component {

	constructor(props) {
		super(props)
	}

	render() {
		console.log(Bar, 'Bar')
		return (
			<Bar data={['1', '2', '3']} width={400} height={400}/>
		)
	}
}

export default Graph
