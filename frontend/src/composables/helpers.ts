export function formatBytes(bytes: number) {
  if (!bytes) return '0 B'
  const sizes = ['B', 'KB', 'MB', 'GB', 'TB']
  const i = Math.floor(Math.log(bytes) / Math.log(1024))
  return Math.max(0, (bytes / Math.pow(1024, i))).toFixed(2) + ' ' + sizes[i]
}

export function filterProperties<
  T extends object,
  K extends keyof T
>(
  obj: T,
  keys: K[],
  silentError: boolean = true
): Pick<T, K> {
  const result = {} as Pick<T, K>

  for (const key of keys) {
    if (key in obj) {
      result[key] = obj[key]
    } else if (!silentError) {
      throw new Error(`Missing property: ${String(key)}`)
    }
  }

  return result
}