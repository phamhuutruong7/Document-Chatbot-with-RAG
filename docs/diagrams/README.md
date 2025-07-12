# 📊 System Diagrams

## 📁 Available Diagrams

This folder contains various system diagrams in Mermaid format (.mmd files) to help visualize the Document Chatbot architecture and data flows.

### 🏗️ Architecture Diagrams
- **[System Architecture](./system-architecture.mmd)** - High-level system overview
- **[Component Diagram](./component-diagram.mmd)** - Component relationships and dependencies

### 🔄 Flow Diagrams
- **[Data Flow](./data-flow.mmd)** - Data processing flows
- **[Sequence Diagram](./sequence-diagram.mmd)** - Interaction sequences

## 🔧 How to View Diagrams

### Online Viewers
- **GitHub**: Diagrams render automatically in GitHub
- **Mermaid Live Editor**: https://mermaid.live/
- **VS Code**: Install Mermaid Preview extension

### Local Viewing
1. Install Mermaid CLI: `npm install -g @mermaid-js/mermaid-cli`
2. Generate images: `mmdc -i diagram.md -o diagram.png`

## 📝 Diagram Conventions

- **Blue**: External services (OpenAI, Pinecone)
- **Green**: Core application components
- **Orange**: Data storage components
- **Purple**: User interface components
- **Red**: Error/exception flows

---

**Note**: All diagrams are maintained in sync with the actual system architecture. Please update diagrams when making architectural changes.