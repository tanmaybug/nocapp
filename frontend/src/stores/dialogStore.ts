import { defineStore } from 'pinia'

export type DialogType = 'ALERT' | 'CONFIRM'

export type Dialog = {
  type: DialogType,
  title: string,
  message: string,
  onConfirm?: () => void,
  onCancel?: () => void
}

export const useDialogStore = defineStore('dialog', {
  state: (): {
    dialogs: Dialog[],
    isVisible: boolean
  } => ({
    dialogs: [],
    isVisible: false,
  }),
  getters: {
    currentDialog(state): Dialog | null {
      return state.dialogs.length > 0 ? state.dialogs[0] : null
    }
  },
  actions: {
    showDialog(dialog: Dialog ) {
      this.dialogs.push(dialog)
      
      if(this.dialogs.length === 1) {
        this.isVisible = true
      }
    },
    hideDialog() {
      this.isVisible = false
      this.dialogs.shift()

      if(this.dialogs.length) {
        this.isVisible = true
        
        const timeout = setTimeout(() => {
          this.hideDialog()
          clearTimeout(timeout)
        }, 1000)
      }
    },
  },
})

export default useDialogStore
