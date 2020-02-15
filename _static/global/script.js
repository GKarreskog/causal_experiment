// Constants that decide the look of graphs
const nodeRadius = 30
const lineHeight = 1
const arrowSize = 10
const arrowColor = '#000'

const mkEl = html => {
  const template = document.createElement('template')
  template.innerHTML = html.trim()
  return template.content.firstChild
}


const drawNode = (root, node) => {
  root.appendChild(
    mkEl(`
      <div
        class="node node-${node.id} ${node.status}"
        id="node-${node.id}"
        style="
          left: ${node.x - nodeRadius}px;
          top: ${node.y - nodeRadius}px;
          height: ${2 * nodeRadius}px;
          width: ${2 * nodeRadius}px;
          line-height: ${2 * nodeRadius}px; /* center vertically */
        "
      >
      ${node.name}
      </div>
    `)
  )
}

const drawArrow = (root, sourceNode, targetNode) => {
  const length = Math.sqrt(
    Math.pow(targetNode.x - sourceNode.x, 2) +
    Math.pow(targetNode.y - sourceNode.y, 2)
  )
  let angleDeg = Math.asin((targetNode.y - sourceNode.y) / length) * 180 / Math.PI
  if ((targetNode.x - sourceNode.x) < 0) {
    angleDeg = 180 - angleDeg
  }
  root.appendChild(
    mkEl(`
      <div
        class="arrow"
        style="
          left: ${(targetNode.x + sourceNode.x) / 2 - length / 2}px;
          top: ${(targetNode.y + sourceNode.y) / 2 - lineHeight / 2}px;
          height: ${lineHeight}px;
          width: ${length}px;
          transform: rotate(${angleDeg}deg);
          background: ${arrowColor};
        "
      >
        <div
          class="arrow-head"
          style="
            border-top: ${arrowSize}px solid transparent;
            border-bottom: ${arrowSize}px solid transparent;
            border-left: ${arrowSize}px solid ${arrowColor};
            left: ${length - nodeRadius - arrowSize}px;
            top: -${arrowSize - lineHeight / 2}px;
          "
        />
      </div>
    `)
  )
}


const drawGraph = (graph, root) => {
  for (const arrow of graph.arrows) {
    const sourceNode = graph.nodes.find(node => node.id === arrow.source)
    const targetNode = graph.nodes.find(node => node.id === arrow.target)
    drawArrow(root, sourceNode, targetNode)
  }
  for (const node of graph.nodes) {
    drawNode(root, node)
  }
}

const mainDraw = (id, graph) => {
  const root = document.getElementById(id)
  drawGraph(graph, root)
}
